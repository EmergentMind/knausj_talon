# XXX - would be nice to be able pipe these through formatters

import sys
from typing import Set

from talon import Context, Module, actions

mod = Module()
mod.list("abbreviation", desc="Common abbreviation")


@mod.capture
def abbreviation(m) -> str:
    "One abbreviation"


ctx = Context()
ctx.lists["user.abbreviation"] = {
    "address": "addr",
    "administrator": "admin",
    "administrators": "admins",
    "advance": "adv",
    "advanced": "adv",
    "alberta": "AB",
    "alternative": "alt",
    "application": "app",
    "applications": "apps",
    "argument": "arg",
    "arguments": "args",
    "as far as I can tell": "afaict",
    "as far as I know": "afaik",
    "assembly": "asm",
    "at the moment": "atm",
    "attribute": "attr",
    "attributes": "attrs",
    "authenticate": "auth",
    "authentication": "auth",
    "away from keyboard": "afk",
    "binary": "bin",
    "british columbia": "BC",
    "button": "btn",
    "canada": "CA",
    "centimeter": "cm",
    "char": "chr",
    "character": "char",
    "class": "cls",
    "client": "cli",
    "command": "cmd",
    "comment": "cmt",
    "compare": "cmp",
    "config": "cfg",
    "configuration": "cfg",
    "context": "ctx",
    "control": "ctrl",
    "constant": "const",
    "coordinate": "coord",
    "coordinates": "coords",
    "copy": "cpy",
    "count": "cnt",
    "counter": "ctr",
    "database": "db",
    "declare": "decl",
    "declaration": "decl",
    "debug": "dbg",
    "define": "def",
    "definition": "def",
    "description": "desc",
    "develop": "dev",
    "development": "dev",
    "dictation": "dict",
    "dictionary": "dict",
    "direction": "dir",
    "directory": "dir",
    "document": "doc",
    "documents": "docs",
    "double": "dbl",
    "dupe": "dup",
    "duplicate": "dup",
    "dynamic": "dyn",
    "enumerate": "enum",
    "environment": "env",
    "escape": "esc",
    "etcetera": "etc",
    "example": "ex",
    "exception": "exc",
    "execute": "exec",
    "expression": "exp",
    "extend": "ext",
    "extension": "ext",
    "file system": "fs",
    "framework": "fw",
    "function": "func",
    "funny": "lol",
    "history": "hist",
    "image": "img",
    "information": "info",
    "initialize": "init",
    "initializer": "init",
    "in real life": "irl",
    "instance": "inst",
    "integer": "int",
    "interrupt": "int",
    "iterate": "iter",
    "java archive": "jar",
    "javascript": "js",
    "jason": "json",
    "jump": "jmp",
    "keyboard": "kbd",
    "keyword arguments": "kwargs",
    "keyword": "kw",
    "kilogram": "kg",
    "kilometer": "km",
    "language": "lng",
    "length": "len",
    "library": "lib",
    "manitoba": "MB",
    "markdown": "md",
    "message": "msg",
    "metasploit": "msf",
    "milligram": "mg",
    "millisecond": "ms",
    "miscellaneous": "misc",
    "module": "mod",
    "mount": "mnt",
    "nano second": "ns",
    "neo vim": "nvim",
    "new brunswick": "NB",
    "nova scotia": "NS",
    "number": "num",
    "object": "obj",
    "okay": "ok",
    "ontario": "ON",
    "operating system": "os",
    "original": "orig",
    "package": "pkg",
    "parameter": "param",
    "parameters": "params",
    "pico second": "ps",
    "pixel": "px",
    "point": "pt",
    "pointer": "ptr",
    "position": "pos",
    "position independent code": "PIC",
    "position independent executable": "PIE",
    "previous": "prev",
    "property": "prop",
    "public": "pub",
    "python": "py",
    "quebec": "QC",
    "query string": "qs",
    "random": "rnd",
    "receipt": "rcpt",
    "reference": "ref",
    "references": "refs",
    "register": "reg",
    "registery": "reg",
    "regular expression": "regex",
    "regular expressions": "regex",
    "represent": "repr",
    "representation": "repr",
    "request": "req",
    "return": "ret",
    "revision": "rev",
    "ruby": "rb",
    "saskatchewan": "SK",
    "service pack": "sp",
    "session id": "sid",
    "shell": "sh",
    "shellcode": "sc",
    "source": "src",
    "special": "spec",
    "specific": "spec",
    "specification": "spec",
    "specify": "spec",
    "standard in": "stdin",
    "standard out": "stdout",
    "standard": "std",
    "string": "str",
    "structure": "struct",
    "synchronize": "sync",
    "synchronous": "sync",
    "system": "sys",
    "table of contents": "toc",
    "table": "tbl",
    "taiwan": "TW",
    "technology": "tech",
    "temporary": "tmp",
    "text": "txt",
    "token": "tok",
    "ultimate": "ulti",
    "unique id": "UUID",
    "user": "usr",
    "utilities": "utils",
    "utility": "util",
    "value": "val",
    "variable": "var",
    "verify": "vrfy",
    "versus": "vs",
    "visual": "vis",
    "visual studio": "MSVC",
    "what the fuck": "wtf",
    "window": "win",
}


@ctx.capture(rule="{user.abbreviation}")
def abbreviation(m):
    return m.abbreviation
