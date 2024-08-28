# In "sqlalchemy", you have
# * engine and connection
# * pools for said connection
# * sql expression language
# * and types for said language
import sqlalchemy
# In "orm", you have
# * session, transaction management
# * mappers
# * attributes, properties, relationships
# * loading strategies
# * the unit of work system
# * instance and attribute states
import sqlalchemy.orm

# For imports, SQLAlchemy uses sqlalchemy.util.preloaded._ModuleRegistry,
# which I tried a little to understand in issue38884.sqlalchemy_import_threadsafety.

