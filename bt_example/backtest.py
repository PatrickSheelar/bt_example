import bt
import matplotlib.pyplot as plt


def run_backtest():
    # Fetch some data
    data = bt.get('spy,agg', start='2010-01-01')
    print(data.head())

    # Create the strategy
    s = bt.Strategy('s1', [bt.algos.RunMonthly(),
                           bt.algos.SelectAll(),
                           bt.algos.WeighEqually(),
                           bt.algos.Rebalance()])

    # Create a backtest and run it
    test = bt.Backtest(s, data)
    res = bt.run(test)

    # Plot the equity curve
    res.plot()
    plt.show()

    # Display stats
    res.display()

    # Plot the return distribution histogram
    res.plot_histogram()
    plt.show()

    # Plot the security weights over time
    res.plot_security_weights()
    plt.show()

if __name__ == '__main__':
    run_backtest()

