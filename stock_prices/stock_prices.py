#!/usr/bin/python

import argparse

def find_max_profit(prices):
  minimum_price = prices[0]
  maximum_profit = prices[1] - prices[0]

  for index in range(1, len(prices)):
    price = prices[index]
    maximum_profit = max(price - minimum_price, maximum_profit)
    minimum_price = min(price, minimum_price)

  return maximum_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_maximum_profit(args.integers), prices=args.integers))