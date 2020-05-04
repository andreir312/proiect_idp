FROM grafana/grafana:latest

ENV GF_SECURITY_ADMIN_PASSWORD secret

COPY datasource.yml /etc/grafana/provisioning/datasources/

COPY dashboard.* /etc/grafana/provisioning/dashboards/
