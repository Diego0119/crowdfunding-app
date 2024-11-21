# Plataforma de Crowdfunding

Este proyecto corresponde a la **Tarea III de Bases de Datos II**. La aplicación es una plataforma de crowdfunding que permite a los usuarios crear y financiar proyectos, utilizando una API RESTful y una base de datos relacional.

## **Integrantes**
- Diego Sanhueza
- Felipe Carcamo

---

## **Objetivos**
- Aplicar los conocimientos adquiridos en el curso para desarrollar una aplicación web con autenticación, autorización y una base de datos relacional.

- Implementar un sistema de gestión de proyectos de crowdfunding que permita a los usuarios interactuar tanto desde el frontend como desde el backend.

---

## **Características de la Plataforma**
1. **Gestión de proyectos**:
   - Creación de proyectos con nombre, descripción, monto objetivo, fechas límite, categoría y recompensas.
   - Visualización del porcentaje de financiamiento alcanzado y número de contribuciones.
   - Cancelación automática de proyectos que no alcanzan el monto objetivo antes de la fecha límite.
   - Evaluación de proyectos al finalizar, con puntuaciones y comentarios visibles.

2. **Gestión de contribuciones**:
   - Registro de aportes económicos por usuarios, con monto y método de pago.
   - Actualización automática del progreso de financiamiento de cada proyecto.

3. **Perfiles de usuario**:
   - Información sobre la cantidad de proyectos creados y en los que ha contribuido.

4. **Sistema de autenticación y autorización**:
   - Registro, inicio de sesión y autorización basada en roles (administrador/usuario).

---

## **Tecnologías Utilizadas**
### **Backend**
- **Lenguaje**: Python
- **Framework**: Litestar
- **ORM**: SQLAlchemy
- **Migraciones**: Alembic

### **Frontend**
- Por definir ....

### **Base de Datos**
- **Sistema Gestor**: Por definir
- **Modelo**: Relacional con al menos 5 tablas