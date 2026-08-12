# ==========================================
# ETAPA 1: Constructor (Builder)
# ==========================================
FROM python:3.12-slim AS builder

# Crear directorio de trabajo
WORKDIR /app

# Variables de entorno para optimizar Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependencias del sistema necesarias para compilar
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copiar requerimientos y compilar en formato "wheel" (mucho más rápido y ligero)
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# ==========================================
# ETAPA 2: Producción (Final)
# ==========================================
FROM python:3.12-slim

WORKDIR /app

# Copiar las librerías pre-compiladas de la Etapa 1
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

# Instalar las librerías limpias
RUN pip install --no-cache /wheels/*

# Copiar todo el código de tu proyecto Django al contenedor
COPY . .

# Exponer el puerto donde correrá Gunicorn
EXPOSE 8000

# Comando de arranque del servidor profesional
CMD ["gunicorn", "myproyect.wsgi:application", "--bind", "0.0.0.0:8000"]