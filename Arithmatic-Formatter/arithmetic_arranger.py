def arithmetic_arranger(problems, results=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  problems_arranged = ""
  first_line = ""
  second_line = ""
  dotted_line = ""
  results_line = ""

  for problem in problems:
    Sections = problem.split()
    Digit1 = Sections[0]
    Digit2 = Sections[2]
    Operator = Sections[1]

    if Operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    if not Digit1.isdigit() or not Digit2.isdigit():
      return "Error: Numbers must only contain digits."

    if len(Digit1) > 4 or len(Digit2) > 4:
      return "Error: Numbers cannot be more than four digits."

    width = max(len(Digit1), len(Digit2)) + 2
    first_line += Digit1.rjust(width) + "    "
    second_line += Operator + Digit2.rjust(width - 1) + "    "
    dotted_line += "-" * width + "    "

    if results:
      if Operator == '+':
        result = str(int(Digit1) + int(Digit2))
      elif Operator == '-':
        result = str(int(Digit1) - int(Digit2))

      results_line += result.rjust(width) + "    "

    problems_arranged = first_line.rstrip() + '\n' + second_line.rstrip(
    ) + '\n' + dotted_line.rstrip()

    if results:
      problems_arranged += '\n' + results_line.rstrip(
    )

  return problems_arranged
