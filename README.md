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
