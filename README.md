flake8-require-beartype
===========

flake8 plugin which checks for use of @beartype decorator.

It checks any function or method that has arguments other
than self, cls, or mcls

## installation

`pip install flake8-require-beartype`

## flake8 codes

| Code   | Description                                            |
|--------|--------------------------------------------------------|
| RBT001 |  Function missing @beartype                            |
| RBT002 |  Method missing @beartype                              |

## rationale

Helps to add / keep beartype runtime checking in a code base.


## as a pre-commit hook

See [pre-commit](https://github.com/rbroderi/precommithooks) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/rbroderi/precommithooks
    rev: HEAD
    hooks:
    -   id: require-beartype
        additional_dependencies: [beartype]
```
