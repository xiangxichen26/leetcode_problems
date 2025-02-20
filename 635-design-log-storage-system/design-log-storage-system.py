class LogSystem:

    def __init__(self):
        self.storage = []
        self.time_dict = {"Year":0, "Month":1, "Day":2, "Hour":3, "Minute":4, "Second":5}
        
    def put(self, id: int, timestamp: str) -> None:
        time = timestamp.split(":")
        mod_time = [time[0],time[0]+time[1],time[0]+time[1]+time[2], time[0]+time[1]+time[2]+time[3], time[0]+time[1]+time[2]+time[3]+time[4], time[0]+time[1]+time[2]+time[3]+time[4]+time[5]]
        self.storage.append([id, mod_time])

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        res = []
        index = self.time_dict[granularity]
        start_time = start.split(":")
        end_time = end.split(":")
        st,et = "",""
        for i in range(index+1):
            st += start_time[i]
            et += end_time[i]
        
        # store the storage 
        modified_storage = sorted(self.storage, key = lambda x:x[1][index]) # 以time的颗粒度排序
        for i in modified_storage:
            if i[1][index] >= st and i[1][index] <= et:
                res.append(i[0])
        
        return res

        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)