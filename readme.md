# ElasticOsiris
### A retarded solution in a  repository because the HU does not have a API to query courses and studies

The `input.json` has been created by allowing my browser to query the maximum amount of documents available from the Elasticsearch back-end storing all the courses and studies.

`result.json` is the filtered version of the `input.json` in a dictionary format with each course as value and each studie as key.

The last part of the project is a snippet that creates a ddl type of script to fill a database for a school project, you can ignore this.

## Insert into db
```
bash-5.1# psql -v ON_ERROR_STOP=1 -1 -h 127.0.0.1 -W -U stutoradmin -f test.sql stutor

INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
```

## To Do:
Make sure to remove special icons ('"\/|) for smooth db execution