
. ./venv/bin/activate

python -m pytest test_app.py

PYTESST_EXIT_CODE=$?


#return if passed or failed(0 or 1)
if [ $PYTESST_EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi