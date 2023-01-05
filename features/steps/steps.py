from behave import given, when, then


@when('somar "{num1:d}" e "{num2:d}"')
def testando_soma(context, num1, num2):
    context.num1 = num1
    context.num2 = num2


@then('o resultado deve ser "{soma:d}"')
def assert_result(context, soma):
    context.result = context.num1 + context.num2
    assert context.result == soma
