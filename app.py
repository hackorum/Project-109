import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as pg

df = pd.read_csv("csv/data.csv")

# I have taken the reading scores
reading_score_list = df["reading score"].tolist()

reading_score_mean = statistics.mean(reading_score_list)
reading_score_median = statistics.median(reading_score_list)
reading_score_mode = statistics.mode(reading_score_list)

standard_deviation = statistics.stdev(reading_score_list)

reading_score_first_stdev_start = reading_score_mean - standard_deviation
reading_score_first_stdev_end = reading_score_mean + standard_deviation
reading_score_second_stdev_start = reading_score_mean - (2 * standard_deviation)
reading_score_second_stdev_end = reading_score_mean + (2 * standard_deviation)
reading_score_third_stdev_start = reading_score_mean - (3 * standard_deviation)
reading_score_third_stdev_end = reading_score_mean + (3 * standard_deviation)

list_of_data_in_first_stdev = [
    result for result in reading_score_list
    if result > reading_score_first_stdev_start and result < reading_score_first_stdev_end
]
list_of_data_in_second_stdev = [
    result for result in reading_score_list
    if result > reading_score_second_stdev_start and result < reading_score_second_stdev_end
]
list_of_data_in_third_stdev = [
    result for result in reading_score_list
    if result > reading_score_third_stdev_start and result < reading_score_third_stdev_end
]

print(
    f"{len(list_of_data_in_first_stdev) * 100 / len(reading_score_list)}% of data is between first standard deviation"
)
print(
    f"{len(list_of_data_in_second_stdev) * 100 / len(reading_score_list)}% of data is between second standard deviation"
)
print(
    f"{len(list_of_data_in_third_stdev) * 100 / len(reading_score_list)}% of data is between third standard deviation"
)

fig = ff.create_distplot([reading_score_list], ["Reading Scores"],
                         show_hist=False)
fig.add_trace(
    pg.Scatter(x=[reading_score_mean, reading_score_mean],
               y=[0, 0.2],
               mode="lines",
               name="Mean"))
fig.add_trace(
    pg.Scatter(
        x=[reading_score_first_stdev_start, reading_score_first_stdev_start],
        y=[0, 0.2],
        mode="lines",
        name="First Standard Deviation",
    ))
fig.add_trace(
    pg.Scatter(
        x=[reading_score_first_stdev_end, reading_score_first_stdev_end],
        y=[0, 0.2],
        mode="lines",
        name="First Standard Deviation",
    ))
fig.add_trace(
    pg.Scatter(
        x=[reading_score_second_stdev_start, reading_score_second_stdev_start],
        y=[0, 0.2],
        mode="lines",
        name="Second Standard Deviation",
    ))
fig.add_trace(
    pg.Scatter(
        x=[reading_score_second_stdev_end, reading_score_second_stdev_end],
        y=[0, 0.2],
        mode="lines",
        name="Second Standard Deviation",
    ))

fig.add_trace(
    pg.Scatter(
        x=[reading_score_third_stdev_start, reading_score_third_stdev_start],
        y=[0, 0.2],
        mode="lines",
        name="Third Standard Deviation",
    ))
fig.add_trace(
    pg.Scatter(
        x=[reading_score_third_stdev_end, reading_score_third_stdev_end],
        y=[0, 0.2],
        mode="lines",
        name="Third Standard Deviation",
    ))

fig.show()
