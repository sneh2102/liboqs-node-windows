{
  "targets": [
    {
      "target_name": "liboqs_node",
      "sources": [
        "./src/addon.cpp",
        "./src/KEMs.cpp",
        "./src/KeyEncapsulation.cpp",
        "./src/Random.cpp",
        "./src/Signature.cpp",
        "./src/Sigs.cpp"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "./deps/liboqs/build/include",
        "./deps/liboqs-cpp/include",
        "C:/Program Files/OpenSSL-Win64/include"
      ],
      "defines": [
        "NAPI_CPP_EXCEPTIONS",
        "NAPI_VERSION=6"
      ],
      "conditions": [
        ["OS=='win'", {
          "libraries": [
            "../deps/liboqs/build/lib/Debug/oqs.lib",
            "../deps/liboqs/build/lib/Debug/oqs-internal.lib",
            "C:/Program Files/OpenSSL-Win64/lib/libcrypto.lib",
            "C:/Program Files/OpenSSL-Win64/lib/libssl.lib"
          ],
          "msvs_settings": {
            "VCCLCompilerTool": {
              "ExceptionHandling": 1 
            }
          }
        }]
      ]
    }
  ]
}