{
  'variables' : {
    'march': '<!(echo ${FARMHASH_MARCH:-native})',
    },
  'targets': [{
    'target_name': 'farmhash',
    'sources': [
       'src/upstream/farmhash.cc',
       'src/bindings.cc'
    ],
    'include_dirs': [
      '<!(node -e "require(\'nan\')")'
    ],
    'cflags_cc': [
        '-fexceptions',
        '-Wall',
        '-march=<(march)',
        '-Ofast',
        '-flto',
        '-funroll-loops'
    ],
    'conditions': [
      [ 'OS=="win"', {
        'defines': [
          'FARMHASH_OPTIONAL_BUILTIN_EXPECT'
        ]
      }]
    ],
    'xcode_settings': {
      'OTHER_CPLUSPLUSFLAGS': [
        '-fexceptions',
        '-Wall',
        '-march=<(march)',
        '-Ofast',
        '-funroll-loops'
      ]
    },
    'configurations': {
      'Release': {
        'msvs_settings': {
          'VCCLCompilerTool': {
            'ExceptionHandling': 1,
          }
        }
      }
    }
  }, {
    'target_name': 'farmhash-legacy',
    'defines': [
      'FARMHASH_LEGACY'
    ],
    'sources': [
       'src/upstream/farmhash-legacy.cc',
       'src/bindings.cc'
    ],
    'include_dirs': [
      '<!(node -e "require(\'nan\')")'
    ],
    'cflags_cc': [
        '-fexceptions',
        '-Wall',
        '-march=<(march)',
        '-Ofast',
        '-flto',
        '-funroll-loops'
    ],
    'conditions': [
      [ 'OS=="win"', {
        'defines': [
          'FARMHASH_OPTIONAL_BUILTIN_EXPECT'
        ]
      }]
    ],
    'xcode_settings': {
      'OTHER_CPLUSPLUSFLAGS': [
        '-fexceptions',
        '-Wall',
        '-march=<(march)',
        '-Ofast',
        '-funroll-loops'
      ]
    },
    'configurations': {
      'Release': {
        'msvs_settings': {
          'VCCLCompilerTool': {
            'ExceptionHandling': 1,
          }
        }
      }
    }
  }]
}
