import redis.clients.jedis.Jedis;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class work_app {

    public static void main(String args[]) throws InterruptedException {
        Connection postgres = null;

        while (postgres == null) {
            try {
                Class.forName("org.postgresql.Driver");
                String url = "jdbc:postgresql://postgres:5432/postgres";
                postgres = DriverManager.getConnection(url, "postgres",
                    "secret");
                postgres.setAutoCommit(false);
            } catch (Exception e) {
                Thread.sleep(1000);
            }
        }

        Jedis redis = null;

        while (true) {
            try {
                redis = new Jedis("redis");
                redis.ping();
                break;
            } catch (Exception e) {
                Thread.sleep(1000);
            }
        }

        while (true) {
            try {
                String name = redis.brpop(0, "singles").get(1);
                PreparedStatement select = postgres.prepareStatement(
                    "SELECT 1" +
                    " FROM singles" +
                    " WHERE NAME = ?" +
                    " FOR UPDATE;"
                );
                select.setString(1, name);
                select.executeQuery();
                PreparedStatement update = postgres.prepareStatement(
                    "UPDATE singles" +
                    " SET count = count + 1" +
                    " WHERE NAME = ?;"
                );
                update.setString(1, name);
                update.executeUpdate();
                postgres.commit();
            } catch (Exception e) {
                continue;
            }
        }
    }

}
