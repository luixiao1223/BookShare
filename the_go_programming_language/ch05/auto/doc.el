(TeX-add-style-hook
 "doc"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("inputenc" "utf8")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "CJKutf8"
    "lmodern"
    "amssymb"
    "amsmath"
    "ifxetex"
    "ifluatex"
    "fixltx2e"
    "fontenc"
    "inputenc"
    "textcomp"
    "unicode-math"
    "upquote"
    "microtype"
    "parskip"
    "hyperref"
    "color"
    "fancyvrb")
   (TeX-add-symbols
    '("WarningTok" 1)
    '("VerbatimStringTok" 1)
    '("VariableTok" 1)
    '("StringTok" 1)
    '("SpecialStringTok" 1)
    '("SpecialCharTok" 1)
    '("RegionMarkerTok" 1)
    '("PreprocessorTok" 1)
    '("OtherTok" 1)
    '("OperatorTok" 1)
    '("NormalTok" 1)
    '("KeywordTok" 1)
    '("InformationTok" 1)
    '("ImportTok" 1)
    '("FunctionTok" 1)
    '("FloatTok" 1)
    '("ExtensionTok" 1)
    '("ErrorTok" 1)
    '("DocumentationTok" 1)
    '("DecValTok" 1)
    '("DataTypeTok" 1)
    '("ControlFlowTok" 1)
    '("ConstantTok" 1)
    '("CommentVarTok" 1)
    '("CommentTok" 1)
    '("CharTok" 1)
    '("BuiltInTok" 1)
    '("BaseNTok" 1)
    '("AttributeTok" 1)
    '("AnnotationTok" 1)
    '("AlertTok" 1)
    "VerbBar"
    "VERB"
    "tightlist"
    "oldparagraph"
    "oldsubparagraph")
   (LaTeX-add-labels
    "ux51fdux6570ux58f0ux660e"
    "example"
    "ux540cux7c7bux578bux53efux4ee5ux653eux5728ux4e00ux8d77"
    "ux9700ux8981ux6ce8ux610fux70b9"
    "ux9012ux5f52"
    "ux591aux503cux8fd4ux56de"
    "ux5ffdux7565ux53c2ux6570"
    "ux4f20ux9012ux53c2ux6570"
    "ux6709ux7684ux51fdux6570ux4e5fux63a5ux53d7ux591aux8fd4ux56deux503cux51fdux6570ux4f5cux4e3aux591aux53c2ux6570"
    "ux88f8ux8fd4ux56de"
    "ux9519ux8bef"
    "ux76f4ux63a5ux5411ux4e0aux4e00ux5c42ux8c03ux7528ux8005ux6c47ux62a5"
    "ux91cdux8bd5ux82e5ux5e72ux6b21ux518dux62a5ux9519ux9000ux51fa"
    "ux76f4ux63a5ux7ec8ux6b62ux7a0bux5e8f"
    "ux67d0ux4e9bux60c5ux51b5ux4e0bux53eaux662fux8bb0ux5f55ux9519ux8befux4fe1ux606fux7136ux540eux7ee7ux7eedux8fd0ux884c"
    "ux76f4ux63a5ux5ffdux7565ux6389ux9519ux8bef"
    "ux51fdux6570ux53d8ux91cf"
    "ux533fux540dux51fdux6570"
    "ux95edux5305ux7684ux6982ux5ff5"
    "ux5bb9ux6613ux51faux9519ux7684ux5730ux65b9"
    "wrong"
    "right"
    "ux53d8ux957fux51fdux6570"
    "ux7b49ux4ef7ux8c03ux7528"
    "ux4e0dux540cux7c7bux578b"
    "ux5ef6ux8fdfux51fdux6570"
    "defer"
    "ux6ce8ux610f"
    "ux6539ux53d8ux8fd4ux56deux503cux7ed3ux679c"
    "ux6587ux4ef6ux63cfux8ff0ux7b26ux5e94ux7528"
    "ux53efux80fdux4f1aux8017ux5c3dux6587ux4ef6ux63cfux8ff0ux7b26ux8d44ux6e90"
    "ux66f4ux597dux7684ux65b9ux6cd5"
    "ux5b95ux673apanic"
    "ux6ce8ux610f-1"
    "runtime"
    "ux6062ux590d")
   (LaTeX-add-environments
    "Shaded"))
 :latex)

