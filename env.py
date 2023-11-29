
import sys
import os

def RunCmd(cmd):
  os.system(cmd)


print("clone Vundle")
cmd = "git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim"

#RunCmd(cmd)

vim_rc = '''
set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

Plugin 'preservim/nerdtree'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
" Plugin 'L9'
" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
" Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
" Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}

" All of your Plugins must be added before the following line
call vundle#end()            " required


set wildmenu " vim自身命令行模式智能补全
set ruler " 在右下角显示光标当前位置信息
set tabstop=2 " 设置制表符占用空格数
set shiftwidth=2
set softtabstop=2
set smartindent
set autoindent
set ai " 自动缩进
set expandtab " 空格代替tab
set number " 行号显示
set hlsearch " 高亮显示结果
set showcmd " 在命令行显示当前输入的命令
set wrap " 打开折行
set completeopt=longest,menu " 取消补全内容以分割子窗口形式出现，只显示补全列表
set fileencodings=ucs-bom,utf-8,cp936,gb18030,big5,euc-jp,sjis,euc-kr,ucs-2le,latin1 "字符编码检测
set textwidth=0 " 关闭自动换行
syntax enable " 开启语法高亮功能
syntax on " 允许用指定语法高亮配色方案替换默认方案
filetype plugin indent on    " required

"设置子窗口的宽度
let Tlist_WinWidth=30
let NERDTreeWinSize=30

" ####### 定义快捷键 #######
let mapleader="," " 定义快捷键的前缀，即<Leader>

" 设置快捷键将选中文本块复制至系统剪贴板
vnoremap <Leader>y "+y 
" 设置快捷键将系统剪贴板内容粘贴至vim
nmap <Leader>p "+p 
"设置显示标签列表子窗口的快捷键。速记：taglist
nnoremap<Leader>tl :TlistToggle<CR>
" 使用NERDTree插件查看工程文件。设置快捷键，速记：file list
nmap <Leader>e :NERDTreeToggle<CR>
" 使用new-omni-completion插件智能补全代码。该插件默认使用CTRL-X CTRL-O补全函数名或变量名，自定义快捷键为TAB
imap <Leader><TAB> <C-X><C-O>

" ####### 函数定义 #######
" vim 高亮显示 glog 行
function SetLogHighLight()
    highlight LogFatal ctermbg=red guifg=red
    highlight LogError ctermfg=red guifg=red
    highlight LogWarning ctermfg=yellow guifg=yellow
    highlight LogInfo ctermfg=green guifg=green
    syntax match LogFatal "^F\d\+ .*$"
    syntax match LogError "^E\d\+ .*$"
    syntax match LogWarning "^W\d\+ .*$"
    "syntax match LogInfo "^I\d\+ .*$"
    syntax match LogInfo "^I[^\]]*\]"
endfunction
autocmd BufEnter *.log.INFO.* call SetLogHighLight()
autocmd BufEnter *.INFO call SetLogHighLight()
autocmd BufEnter *.log.WARNING.* call SetLogHighLight()
autocmd BufEnter *.WARNING call SetLogHighLight()
autocmd BufEnter *.log.ERROR.* call SetLogHighLight()
autocmd BufEnter *.ERROR call SetLogHighLight()
autocmd BufEnter *.log.FATAL.* call SetLogHighLight()
autocmd BufEnter *.FATAL call SetLogHighLight()

" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
'''

homepath = os.path.expanduser('~')
with open(homepath + '/.vimrc', 'w') as f:
  f.write(vim_rc)
