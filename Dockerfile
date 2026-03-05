FROM python:3.12-alpine

WORKDIR /app

COPY index.html /app/index.html
COPY business-navigator-product-prototype.html /app/business-navigator-product-prototype.html
COPY startup-onepager.html /app/startup-onepager.html
COPY google-drive-ready /app/google-drive-ready

EXPOSE 8080

CMD ["sh", "-c", "python -m http.server ${PORT:-8080} --directory /app"]
