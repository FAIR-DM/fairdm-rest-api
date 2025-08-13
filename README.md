# FairDM REST API

A comprehensive REST API implementation for FAIR-DM (FAIR Data Management) that provides programmatic access to scientific data management features. This package extends the core FairDM platform with robust API endpoints for data discovery, management, and integration.

Note: This project is under active development and may undergo significant changes. Contributions and feedback are welcome!

## Overview

The FairDM REST API is built on Django REST Framework and provides a standards-compliant interface for:

- **Project Management**: Access and manage research projects
- **Dataset Operations**: CRUD operations on scientific datasets
- **Sample Management**: Handle various types of scientific samples
- **Measurement Data**: Access measurement data and metadata
- **Identity Management**: User authentication and authorization
- **Terms of Service**: API usage agreements and compliance

## Features

### 🔧 Core API Features
- **RESTful Design**: Standards-compliant REST API endpoints
- **OpenAPI/Swagger Documentation**: Interactive API documentation
- **Geographic Information System (GIS)**: Support for spatial data
- **Flexible Serialization**: Multiple output formats including JSON and pandas-compatible data
- **Access Control**: Fine-grained permissions and access policies
- **Throttling**: Rate limiting for API usage
- **CORS Support**: Cross-origin resource sharing configuration

### 📊 Data Management
- **Project Endpoints**: Manage research projects and metadata
- **Dataset Operations**: Full CRUD operations on datasets
- **Sample Types**: Support for multiple sample types and classifications
- **Measurement Data**: Access to measurement results and associated metadata
- **Polymorphic Models**: Handle diverse data types through polymorphic serialization

### 🔒 Security & Authentication
- **REST Authentication**: Token-based authentication via dj-rest-auth
- **Access Policies**: Role-based access control using drf-access-policy
- **Permission Management**: Granular permission system
- **Secure Headers**: CORS and security headers configuration

## Installation

FairDM REST API is an addon for the FairDM Framework. To use it in your own project, first install it:

```bash
poetry add fairdm-rest-api
```

Then, add it as an addon in your `config/settings.py` file:

```python
import fairdm

fairdm.setup(
    addons=[
        'fairdm_rest_api',
    ],
)
```
That's it! FairDM REST API is now integrated into your portal.

## Configuration

Following the FairDM guidelines for addons, this package is highly-opinionated. It relies on several third-party libraries and has a specific configuration structure to ensure consistency, ease of use, and standardization across multiple unrelated projects.

You can examine the pre-configured settings in `src/fairdm_api/settings.py`. These are automatically integrated into your project. If these settings do not exactly match your needs, you can override them in your own `config/settings.py` file.




## Development

### Dependencies

Key dependencies include:
- **Django REST Framework**: Core API framework
- **drf-spectacular**: OpenAPI documentation
- **djangorestframework-gis**: Geographic data support
- **rest-pandas**: Pandas integration for data serialization
- **dj-rest-auth**: Authentication endpoints
- **django-cors-headers**: CORS support

### Setup your environment

```bash
# Install development dependencies
poetry install

# Run tests
poetry run python manage.py test

# Generate API schema
poetry run python manage.py setup

# Take API screenshots (for documentation)
poetry run python manage.py runserver
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run the test suite: `poetry run python manage.py test`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support and questions:
- **Issues**: Submit issues on the project repository

## Further Reading

- **[FairDM Github](https://github.com/FAIR-DM/fairdm)**
- **[FairDM Documentation](www.fairdm.org)**
