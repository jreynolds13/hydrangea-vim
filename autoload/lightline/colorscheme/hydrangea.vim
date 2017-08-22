" Author:   Yuta Taniguchi <yuta.taniguchi.y.t@gmail.com>
" URL:      https://github.com/yuttie/hydrangea-vim
" Version:  4.1.0
" License:  MIT License

let s:base03       = ["#1e222c", 235]  " L* = 44
let s:base02       = ["#2a303b", 236]  " L* = 50
let s:base01       = ["#373d4b", 237]  " L* = 56
let s:base00       = ["#474e5c", 239]  " L* = 62
let s:base2        = ["#c3d0ec", 252]  " L* = 93
let s:base3        = ["#edf9ff", 231]  " L* = 99
let s:red          = ["#e91e63", 197]
let s:red_dark     = ["#792340",  52]
let s:teal         = ["#36c2c2",  44]
let s:teal_dark    = ["#134242",  23]
let s:blue         = ["#537dd5",  68]
let s:blue_light   = ['#91b5ff', 111]
let s:violet       = ["#996ddb",  98]
let s:violet_light = ["#ceadff", 183]
let s:magenta      = ["#e242ac", 162]

let s:p = {'normal': {}, 'inactive': {}, 'insert': {}, 'replace': {}, 'visual': {}, 'tabline': {}}
let s:p.normal.left     = [ [ s:base03,  s:blue          ], [ s:base2, s:base01 ] ]
let s:p.normal.middle   = [ [ s:base2,   s:base02        ],                       ]
let s:p.normal.right    = [ [ s:base2,   s:base00        ], [ s:base2, s:base01 ] ]

let s:p.insert.left     = [ [ s:base03,  s:teal          ], [ s:base2, s:base01 ] ]

let s:p.visual.left     = [ [ s:base03,  s:violet        ], [ s:base2, s:base01 ] ]
let s:p.replace.left    = [ [ s:base03,  s:magenta       ], [ s:base2, s:base01 ] ]

let s:p.inactive.left   = [ [ s:base03,  s:base00        ], [ s:base03, s:base01 ] ]
let s:p.inactive.middle = [ [ s:base03,  s:base02        ],                       ]
let s:p.inactive.right  = [ [ s:base03,  s:base00        ], [ s:base03, s:base01 ] ]

let s:p.normal.error    = [ [ s:red,     s:base02        ] ]
let s:p.normal.warning  = [ [ s:magenta, s:base01        ] ]

let s:p.tabline.left    = [ [ s:base03,  s:base00        ] ]
let s:p.tabline.middle  = [ [ s:base03,  s:base02        ] ]
let s:p.tabline.right   = [ [ s:base03,  s:base00        ] ]
let s:p.tabline.tabsel  = [ [ s:base03,  s:base2         ] ]

let g:lightline#colorscheme#hydrangea#palette = lightline#colorscheme#flatten(s:p)
