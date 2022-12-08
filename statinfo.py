import csv
import statistics

# Open the CSV file and read the data with open('panel_data.csv', 'r') as csvfile:
    data = csv.reader(csvfile)

    next(data)
    
    sums = {}
    counts = {}
    means = {}
    medians = {}
    modes = {}
    variances = {}
    peaks = {}
    
    for row in data:
        panel_id = row[0]
        
        if panel_id not in sums:
            sums[panel_id] = []
            counts[panel_id] = 0

        sums[panel_id].append(float(row[1]))
        
        counts[panel_id] += 1
    
    for panel_id in sums:
        values = sums[panel_id]
        
        means[panel_id] = sum(values) / counts[panel_id]
        
        medians[panel_id] = statistics.median(values)
        
        modes[panel_id] = statistics.mode(values)
        
        variances[panel_id] = statistics.variance(values)
        
        peaks[panel_id] = max(values)
    
    print('Means:', means)
    print('Medians:', medians)
    print('Modes:', modes)
    print('Variances:', variances)
    print('Peaks:', peaks)
