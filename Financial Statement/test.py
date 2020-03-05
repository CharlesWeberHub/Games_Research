from yahoofinancials import YahooFinancials

game_stocks = ['NTES','YY']

yahoo_financials_game = YahooFinancials(game_stocks)

game_cash_flow_data_an = yahoo_financials_game.get_financial_stmts('annual', 'cash')
game_income_sta_data_an = yahoo_financials_game.get_financial_stmts('annual', 'income')
game_balance_data_an = yahoo_financials_game.get_financial_stmts('annual', 'balance')

print(game_cash_flow_data_an)
print(game_income_sta_data_an)
print(game_balance_data_an)
