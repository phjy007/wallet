#!/bin/sh
export script_type="autogen"
export EX_DEV="~/exdev"
export cwd=${PWD}
export toolkit_path=/home/arthur/.toolkit
export lang_type="unknown"
export vimfiles_path=".vimfiles"
export file_filter="c|C|c\+\+|cc|cp|cpp|cxx|h|H|h\+\+|hh|hp|hpp|hxx|inl|ipp|cs|js|as|java|hlsl|vsh|psh|fx|fxh|cg|shd|glsl|py|pyw|pyx|pxd|lua|wlua|vim|uc|m|wiki|ini|cfg|mak|mk|Makefile|makefile|sh|SH|bsh|bash|ksh|zsh|bat|log|err|exe|qrc|pro|pri|i|swg"
export file_filter_pattern='\\.c$|\\.C$|\\.c++$|\\.cc$|\\.cp$|\\.cpp$|\\.cxx$|\\.h$|\\.H$|\\.h++$|\\.hh$|\\.hp$|\\.hpp$|\\.hxx$|\\.inl$|\\.ipp$|\\.cs$|\\.js$|\\.as$|\\.java$|\\.hlsl$|\\.vsh$|\\.psh$|\\.fx$|\\.fxh$|\\.cg$|\\.shd$|\\.glsl$|\\.py$|\\.pyw$|\\.pyx$|\\.pxd$|\\.lua$|\\.wlua$|\\.vim$|\\.uc$|\\.m$|\\.wiki$|\\.ini$|\\.cfg$|\\.mak$|\\.mk$|\\.Makefile$|\\.makefile$|\\.sh$|\\.SH$|\\.bsh$|\\.bash$|\\.ksh$|\\.zsh$|\\.bat$|\\.log$|\\.err$|\\.exe$|\\.qrc$|\\.pro$|\\.pri$|\\.i$|\\.swg$'
export cscope_file_filter="c|C|c\+\+|cc|cp|cpp|cxx|h|H|h\+\+|hh|hp|hpp|hxx|inl|ipp|hlsl|vsh|psh|fx|fxh|cg|shd|glsl"
export cscope_file_filter_pattern='\\.c$|\\.C$|\\.c++$|\\.cc$|\\.cp$|\\.cpp$|\\.cxx$|\\.h$|\\.H$|\\.h++$|\\.hh$|\\.hp$|\\.hpp$|\\.hxx$|\\.inl$|\\.ipp$|\\.hlsl$|\\.vsh$|\\.psh$|\\.fx$|\\.fxh$|\\.cg$|\\.shd$|\\.glsl$'
export dir_filter=""
export support_filenamelist="false"
export support_ctags="false"
export support_symbol="false"
export support_inherit="false"
export support_cscope="false"
export support_idutils="true"
export ctags_cmd="ctags"
export ctags_options=" --fields=+iaS --extra=+q --languages= --langmap="
if [ -f "./${vimfiles_path}/quick_gen_project_pre_custom.sh" ]; then
    sh ./${vimfiles_path}/quick_gen_project_pre_custom.sh
fi
sh ${toolkit_path}/quickgen/bash/quick_gen_project.sh $1
if [ -f "./${vimfiles_path}/quick_gen_project_post_custom.sh" ]; then
    sh ./${vimfiles_path}/quick_gen_project_post_custom.sh
fi
