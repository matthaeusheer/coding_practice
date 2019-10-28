def run_sub_tests(test_case, func, input_values, solutions):
    for idx, (input_value, expected_solution) in enumerate(zip(input_values, solutions)):
        with test_case.subTest(test_case=idx):
            test_case.assertEqual(expected_solution, func(input_value),
                                  f'Sub test nr. {idx} failed. {func.__name__}({input_value}) '
                                  f'should be {expected_solution}.')