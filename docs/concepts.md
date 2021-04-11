# Concepts

## ETL

Extract Transform Load

## DAGS

Directed Acyclic Graphs

Example: Data pipelines

## Operators

Like an object around the task (that is inside the DAG) you want to execute.

Example:

```py
# Operator

file = open("myfile", "r")
print(f.read())
```

**Types of operators**:

- Action Operator: Python, Bash, Postgres, ...
- Transfer Operator: MysqlToPostgres, ...
- Sensor Operators: FileSensor (wait until file arrive in specific destination to do next task)

## Task

Instance of an Operator

### Task Instance

Represents a specific run of a task: DAG + TASK + Point in time

## Dependencies

Relationships between tasks/OPerators

- `set_upstream` or `<<`
- `set_downstream` or `>>`

Operator A => Operator B => Operator C
