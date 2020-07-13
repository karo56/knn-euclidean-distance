class knn():
    def distance(self, vec1, vec2):
        dist = 0
        n = len(vec1) - 1 # lenght of vec1 and vec2 is equal
        for i in range(n):
            dist += (vec1[i] - vec2[i])**2
        dist = dist**(0.5)
        return dist
    
    
    
    def nearest(self ,new_row, train_data, k):
        distances = {}
        n = len(train_data)
        for i in range(n):
            dist = self.distance(train_data[i], new_row)
            distances[i] = dist
        
        
        
        dist_sorted = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
        neighbors = []
        for i in range(k):
            buff = list(dist_sorted.keys())[i]
            neighbors.append(buff)
        
        return neighbors
    
    
    def predict(self, new_row, train_data, k=5):
        neighbors = self.nearest(new_row, train_data, k)
        values = train_data[neighbors,-1]
        freq = {}
        for i in range(k):
            if values[i] in freq:
                freq[values[i]] += 1
            else:
                freq[values[i]] = 1
            
        prediction = max(freq, key=freq.get)
        
        return prediction
