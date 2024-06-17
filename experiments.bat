@echo off
call env/Scripts/activate.bat
echo Executing f1 experiments...
python main.py --y_func f1 --seed 42
python main.py --y_func f1 --tpa --seed 42
python main.py --y_func f1 --msr --seed 42
python main.py --y_func f1 --tpa --msr --seed 42
echo finished

echo Executing f2 experiments...
python main.py --y_func f2 --seed 42
python main.py --y_func f2 --tpa --seed 42
python main.py --y_func f2 --msr --seed 42
python main.py --y_func f2 --tpa --msr --seed 42
echo finished

echo Executing f3 experiments...
python main.py --y_func f3 --seed 42
python main.py --y_func f3 --tpa --seed 42
python main.py --y_func f3 --msr --seed 42
python main.py --y_func f3 --tpa --msr --seed 42
echo finished

echo Executing f4 experiments...
python main.py --y_func f4 --seed 42
python main.py --y_func f4 --tpa --seed 42
python main.py --y_func f4 --msr --seed 42
python main.py --y_func f4 --tpa --msr --seed 42
echo finished

echo Executing f5 experiments...
python main.py --y_func f5 --seed 42
python main.py --y_func f5 --tpa --seed 42
python main.py --y_func f5 --msr --seed 42
python main.py --y_func f5 --tpa --msr --seed 42
echo finished

echo Executing f6 experiments...
python main.py --y_func f6 --seed 42
python main.py --y_func f6 --tpa --seed 42
python main.py --y_func f6 --msr --seed 42
python main.py --y_func f6 --tpa --msr --seed 42
echo finished

echo Executing f7 experiments...
python main.py --y_func f7 --seed 42
python main.py --y_func f7 --tpa --seed 42
python main.py --y_func f7 --msr --seed 42
python main.py --y_func f7 --tpa --msr --seed 42
echo finished

echo Executing f8 experiments...
python main.py --y_func f8 --seed 42
python main.py --y_func f8 --tpa --seed 42
python main.py --y_func f8 --msr --seed 42
python main.py --y_func f8 --tpa --msr --seed 42
echo finished

echo Executing f9 experiments...
python main.py --y_func f9 --seed 42
python main.py --y_func f9 --tpa --seed 42
python main.py --y_func f9 --msr --seed 42
python main.py --y_func f9 --tpa --msr --seed 42
echo finished

echo Executing f10 experiments...
python main.py --y_func f10 --seed 42
python main.py --y_func f10 --tpa --seed 42
python main.py --y_func f10 --msr --seed 42
python main.py --y_func f10 --tpa --msr --seed 42
echo finished
pause