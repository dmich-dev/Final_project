import traceback
try:
    from src.main import main
    main()
except Exception as e:
    print(f'ERROR: {e}')
    traceback.print_exc()
