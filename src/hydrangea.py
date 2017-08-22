HEADER = """" Name:     hydrangea.vim --- Hydrangea theme for Vim
" Author:   Yuta Taniguchi <yuta.taniguchi.y.t@gmail.com>
" URL:      https://github.com/yuttie/hydrangea-vim
" Version:  4.1.0
" License:  MIT License
"""


from collections import OrderedDict

try:
    import vim

    def execute(cmd):
        vim.command(cmd)
except ImportError:
    print(HEADER)

    def execute(cmd):
        print(cmd)


# Palette
base03       = ("#1e222c", 235)  # L* = 44
base02       = ("#2a303b", 236)  # L* = 50
base01       = ("#373d4b", 237)  # L* = 56
base00       = ("#474e5c", 239)  # L* = 62
base2        = ("#c3d0ec", 252)  # L* = 93
base3        = ("#edf9ff", 231)  # L* = 99
red          = ("#e91e63", 197)
red_dark     = ("#792340",  52)
teal         = ("#36c2c2",  44)
teal_dark    = ("#134242",  23)
blue         = ("#537dd5",  68)
blue_light   = ('#91b5ff', 111)
violet       = ("#996ddb",  98)
violet_light = ("#ceadff", 183)
magenta      = ("#e242ac", 162)
diff_add_fg  = ("#52c4ff",  81)
diff_add_bg  = ("#0d435f",  24)
diff_add_hi  = ("#97dcff", 117)
diff_rm_fg   = ("#e242ac", 162)
diff_rm_bg   = ("#66184c",  53)
diff_rm_hi   = ("#fface3", 218)


# Definitions
color = OrderedDict()
color['Normal']       = {'fg': base2,            'bg': base03,                                   }
color['Cursor']       = {'fg': 'NONE',           'bg': base3,                 'deco': 'NONE'     }
color['CursorIM']     = {'fg': 'NONE',           'bg': base3,                                    }
color['CursorLine']   = {'fg': 'NONE',           'bg': base02,                'deco': 'bold'     }
color['CursorColumn'] = {'fg': 'NONE',           'bg': base02,                'deco': 'NONE'     }
color['Visual']       = {'fg': 'NONE',           'bg': base01,                'deco': 'NONE'     }
color['VisualNOS']    = {'fg': 'fg',                                          'deco': 'underline'}

color['Folded']       = {'fg': base2,            'bg': base02,                'deco': 'NONE'     }
color['FoldColumn']   = {'fg': base2,            'bg': base03,                'deco': 'NONE'     }
color['Title']        = {'fg': magenta,          'bg': 'NONE',                'deco': 'bold'     }
color['StatusLine']   = {'fg': base2,            'bg': base01,                'deco': 'NONE'     }
color['StatusLineNC'] = {'fg': base00,           'bg': base02,                'deco': 'NONE'     }
color['VertSplit']    = {'fg': base02,           'bg': base02,                'deco': 'NONE'     }
color['LineNr']       = {'fg': base00,           'bg': base02,                'deco': 'NONE'     }
color['CursorLineNr'] = {'fg': base3,            'bg': base00,                'deco': 'bold'     }
color['SpecialKey']   = {'fg': teal_dark,        'bg': teal,                  'deco': 'bold'     }
color['NonText']      = {'fg': base00,           'bg': base03,                'deco': 'NONE'     }
color['MatchParen']   = {'fg': red,              'bg': 'NONE',                'deco': 'bold'     }

color['Comment']      = {'fg': base00,                                        'deco': 'NONE'     }
color['Constant']     = {'fg': teal,             "bg": teal_dark,             'deco': 'NONE'     }
color['String']       = 'Constant'
color['Number']       = 'Constant'
color['Identifier']   = {'fg': base3,                                         'deco': 'bold'     }
color['Function']     = {'fg': base3,                                         'deco': 'bold'     }
color['Statement']    = {'fg': blue,                                          'deco': 'bold'     }
color['Operator']     = {'fg': magenta,                                       'deco': 'NONE'     }
color['Include']      = {'fg': violet,                                        'deco': 'NONE'     }
color['PreProc']      = {'fg': violet_light,                                  'deco': 'NONE'     }
color['Type']         = {'fg': magenta,                                       'deco': 'NONE'     }
color['StorageClass'] = {'fg': blue,                                          'deco': 'bold'     }
color['Structure']    = {'fg': magenta,                                       'deco': 'NONE'     }
color['Typedef']      = {'fg': blue,                                          'deco': 'bold'     }
color['Special']      = {'fg': blue_light,       'bg': 'NONE',                'deco': 'bold'     }
color['Underlined']   = {'fg': 'fg',                                          'deco': 'underline'}
color['Ignore']       = {'fg': 'bg'                                                              }
color['Error']        = {'fg': red,              'bg': red_dark,              'deco': 'bold'     }
color['Todo']         = {'fg': base2,            'bg': base03,                'deco': 'bold'     }

color['IncSearch']    = {'fg': base3,            'bg': violet_light,          'deco': 'NONE'     }
color['Search']       = {'fg': base3,            'bg': magenta,               'deco': 'NONE'     }
color['Pmenu']        = {'fg': base2,            'bg': base02,                'deco': 'NONE'     }
color['PmenuSel']     = {'fg': base3,            'bg': base01,                'deco': 'bold'     }
color['PmenuSbar']    = {                        'bg': base02,                'deco': 'NONE'     }
color['PmenuThumb']   = {                        'bg': base00,                'deco': 'NONE'     }
color['TabLine']      = {'fg': base00,           'bg': base02,                'deco': 'NONE'     }
color['TabLineSel']   = {'fg': base03,           'bg': blue,                  'deco': 'bold'     }
color['TabLineFill']  = {'fg': base02,           'bg': base03,                'deco': 'underline'}

color['SpellBad']     = {                                                     'deco': 'undercurl'}
color['SpellCap']     = {                                                     'deco': 'undercurl'}
color['SpellRare']    = {                                                     'deco': 'undercurl'}
color['SpellLocal']   = {                                                     'deco': 'undercurl'}

color['DiffAdd']      = {'fg': diff_add_fg,      'bg': diff_add_bg,           'deco': 'NONE'     }
color['DiffChange']   = {'fg': diff_rm_fg,       'bg': diff_rm_bg,            'deco': 'NONE'     }
color['DiffDelete']   = {'fg': diff_rm_fg,       'bg': diff_rm_bg,            'deco': 'NONE'     }
color['DiffText']     = {'fg': diff_rm_hi,       'bg': diff_rm_bg,            'deco': 'bold'     }

color['diffAdded']    = {'fg': diff_add_fg,      'bg': diff_add_bg,           'deco': 'NONE'     }
color['diffRemoved']  = {'fg': diff_rm_fg,       'bg': diff_rm_bg,            'deco': 'NONE'     }

color['Directory']    = {'fg': teal,                                          'deco': 'NONE'     }
color['ErrorMsg']     = {'fg': red,              'bg': 'NONE',                'deco': 'NONE'     }
color['SignColumn']   = {'fg': base2,            'bg': color['LineNr']['bg'], 'deco': 'NONE'     }
color['MoreMsg']      = {'fg': blue,                                          'deco': 'NONE'     }
color['ModeMsg']      = {                                                     'deco': 'bold'     }
color['Question']     = {'fg': 'fg',                                          'deco': 'NONE'     }
color['WarningMsg']   = {'fg': red,                                           'deco': 'NONE'     }
color['WildMenu']     = {'fg': base3,            'bg': base00,                'deco': 'bold'     }
color['ColorColumn']  = {'fg': 'NONE',           'bg': red_dark,              'deco': 'NONE'     }

# GitGutter
color['GitGutterAdd']    = {'fg': diff_add_fg, 'bg': color['SignColumn']['bg'], 'deco': 'bold'}
color['GitGutterChange'] = {'fg': diff_rm_fg,  'bg': color['SignColumn']['bg'], 'deco': 'bold'}
color['GitGutterDelete'] = {'fg': diff_rm_fg,  'bg': color['SignColumn']['bg'], 'deco': 'bold'}

# make
color['makeIdent']      = 'Type'
color['makeSpecTarget'] = 'Special'
color['makeTarget']     = 'Function'
color['makeCommands']   = 'NONE'

# php
color['phpVarSelector'] = 'Identifier'
color['phpIdentifier']  = 'NONE'
color['phpFunctions']   = 'NONE'
color['phpClasses']     = 'NONE'
color['phpFunction']    = 'Function'
color['phpClass']       = 'Type'

# rust
color['rustFuncCall'] = {'fg': blue_light}
color['rustQuestionMark'] = 'Operator'

# vim
color['vimVar'] = 'NONE'


# Apply
execute("""hi clear
if exists('syntax_on')
  syntax reset
endif
let g:colors_name = 'hydrangea'

set background=dark
""")

HI_ARGS = ['ctermfg', 'ctermbg', 'cterm', 'guifg', 'guibg', 'gui']

links = []
for name, cdef in color.items():
    if type(cdef) is str:
        # The definition is a string
        if cdef == 'NONE':
            # Disable
            execute('hi ' + name + ' NONE')
            links.append('hi link ' + name + ' NONE')
        else:
            # Link
            links.append('hi link ' + name + ' ' + cdef)
    elif type(cdef) is dict and len(cdef) > 0:
        # The definition is a dictionary
        def2 = {}
        for key, val in cdef.items():
            if key == 'fg':
                if type(val) is tuple:
                    def2['guifg'] = val[0]
                    def2['ctermfg'] = val[1]
                elif type(val) is str and val == 'NONE':
                    def2['guifg'] = val
                    def2['ctermfg'] = val
                elif type(val) is str:
                    def2['guifg'] = val
                elif type(val) is int:
                    def2['ctermfg'] = val
            elif key == 'bg':
                if type(val) is tuple:
                    def2['guibg'] = val[0]
                    def2['ctermbg'] = val[1]
                elif type(val) is str and val == 'NONE':
                    def2['guibg'] = val
                    def2['ctermbg'] = val
                elif type(val) is str:
                    def2['guibg'] = val
                elif type(val) is int:
                    def2['ctermbg'] = val
            elif key == 'deco':
                if type(val) is tuple:
                    def2['gui'] = val[0]
                    def2['cterm'] = val[1]
                elif type(val) is str:
                    def2['gui'] = val
                    def2['cterm'] = val
        def2 = sorted(def2.items(), key=lambda x: HI_ARGS.index(x[0]))
        execute('hi ' + name + ' ' + ' '.join(k + '=' + str(v) for k, v in def2))

for link in links:
    execute(link)
