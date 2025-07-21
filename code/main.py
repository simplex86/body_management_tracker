import subm.loader as loader
import subm.ploter as ploter
import subm.helper as helper

data_filename = "./data/data.txt"
plot_filename = "./data/plot.txt"

def main():
    date_data, height_data, weight_data = loader.load_datas(data_filename)
    height_plot, weight_plot, bmi_plot = loader.load_plots(plot_filename)

    bmi_data = helper.get_bmis(height_data, weight_data)

    ploter.set_dates(date_data)
    ploter.set_heights(height_data, height_plot)
    ploter.set_weights(weight_data, weight_plot)
    ploter.set_bmis(bmi_data, bmi_plot)
    ploter.plot()

if __name__ == "__main__":
    main()