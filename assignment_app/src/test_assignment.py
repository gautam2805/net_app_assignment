
from io import StringIO
import sys
from app import main

def test_main_output(capsys):
    # Call the main function
    main()

    # Capture only the printed output from stdout
    captured = capsys.readouterr().out

    # Check the captured output
    expected_output = "Hello Team!\nAssignment completed.\n"
    assert captured == expected_output
