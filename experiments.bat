@echo off
call env/Scripts/activate.bat
echo Executing f5 experiments...
python main.py --y_func f5
python main.py --y_func f5 --tpa
python main.py --y_func f5 --msr
python main.py --y_func f5 --tpa --msr
echo finished

echo Executing f6 experiments...
python main.py --y_func f6
python main.py --y_func f6 --tpa
python main.py --y_func f6 --msr
python main.py --y_func f6 --tpa --msr
echo finished

echo Executing f7 experiments...
python main.py --y_func f7
python main.py --y_func f7 --tpa
python main.py --y_func f7 --msr
python main.py --y_func f7 --tpa --msr
echo finished

echo Executing f8 experiments...
python main.py --y_func f8
python main.py --y_func f8 --tpa
python main.py --y_func f8 --msr
python main.py --y_func f8 --tpa --msr
echo finished

echo Executing f9 experiments...
python main.py --y_func f9
python main.py --y_func f9 --tpa
python main.py --y_func f9 --msr
python main.py --y_func f9 --tpa --msr
echo finished

echo Executing f10 experiments...
python main.py --y_func f10
python main.py --y_func f10 --tpa
python main.py --y_func f10 --msr
python main.py --y_func f10 --tpa --msr
echo finished
pause