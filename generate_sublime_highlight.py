import h4x.stdlib as stdlib

functions = "|".join(stdlib.exports.keys())

syntax = f"""
%YAML 1.2
---
# See http://www.sublimetext.com/docs/syntax.html
file_extensions:
  - h4x
scope: source.h4x
contexts:
  main:
    - match: '"'
      scope: punctuation.definition.string.begin.h4x
      push: double_quoted_string

    - match: '{{'
      scope: punctuation.definition.comment.multiline.h4x
      push: multiline_comment

    - match: '~'
      scope: punctuation.definition.comment.h4x
      push: line_comment

    - match: '\\b({functions})\\b'
      scope: keyword.control.h4x

    - match: '\\b(-)?[0-9.]+\\b'
      scope: constant.numeric.h4x

  double_quoted_string:
    - meta_scope: string.quoted.double.h4x
    - match: '\\.'
      scope: constant.character.escape.h4x
    - match: '"'
      scope: punctuation.definition.string.end.h4x
      pop: true

  multiline_comment:
    - meta_scope: comment.multiline.h4x
    - match: '}}'
      scope: punctuation.definition.comment.multiline.end.h4x
      pop: true

  line_comment:
    - meta_scope: comment.line.h4x
    - match: $
      pop: true
"""

print(syntax)