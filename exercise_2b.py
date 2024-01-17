def earthquake_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            magnitude, date, time, latitude, longitude, depth, *region_parts = line.split(' ') 
            region = ''.join(region_parts[-1])
            data.append((region.strip(), [date, float(magnitude)]))
    return data 

def alaska_data(data):
    alaska = []
    alaska.append(data[0][0])
    alaska.append(data[0][1])
    alaska.append(data[3][1])
    alaska.append(data[5][1])
    alaska.append(data[7][1])
    alaska.append(data[8][1])
    return alaska

def hawaii_data(data):
    hawaii = []
    hawaii.append(data[1][0])
    hawaii.append(data[1][1])
    hawaii.append(data[6][1])
    return hawaii

def mexico_data(data):
    mexico = []
    mexico.append(data[-2][0])
    mexico.append(data[-2][1])
    mexico.append(data[-1][1])
    return mexico

def region_data(data, region_indexs):
    region_data = []
    for index in region_indexs:
        region_data.append(data[index][0])
        region_data.append(data[index][1])
    return region_data
        
def main():
    panama_index = [2]
    missouri_index = [4]
    indonesia_index = [9]
    vanuatu_index = [10]
    data = earthquake_data('earthquake.txt') 
    alaska = alaska_data(data)
    panama = region_data(data, panama_index)
    missouri = region_data(data, missouri_index)
    indonesia = region_data(data, indonesia_index)
    vanuatu = region_data(data, vanuatu_index)
    hawaii = hawaii_data(data)
    mexico = mexico_data(data)
    
main()
