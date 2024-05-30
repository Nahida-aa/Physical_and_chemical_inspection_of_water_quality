@REM 这是一个注释 remark if 不写@就会显示注释 @ 符号的作用是阻止命令本身的输出
:: create a new file (if file is not exist)
@REM IF NOT EXIST .gitignore echo. > .gitignore


:: 如果文件存在，则删除文件
@REM IF EXIST filename.txt del /F filename.txt
del /F .gitignore
@REM Could Not Find path\filename.txt
@REM /F 参数用于强制删除只读文件
@REM 只读是 Windows 系统中的文件属性。如果文件为只读，那么文件就不能被修改或删除
@REM 只读文件的属性可以通过 attrib 命令来查看和修改
@REM attrib filename.txt
@REM attrib +R filename.txt
@REM attrib -R filename.txt
@REM attrib +R -S -H filename.txt
@REM -S 移除系统文件属性 -H：移除隐藏属性

@echo off
@REM 使用了 setlocal 和 endlocal 命令。
@REM 这两个命令可以限制变量的作用范围，使其只在当前的代码块中有效
setlocal
set "files=file1.txt file2.txt file3.txt"
for %%f in (%files%) do (
    if exist %%f (
        echo Deleting %%f
        del /F %%f
    )
)
endlocal