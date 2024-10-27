from bus_service.service.service import *
class path_view:
    def render_path(paths):
        for path in paths:
            total_stops = 0
            changes = len(path)
            total_ac_fare = 0
            total_non_ac_fare = 0

            for sub_path in path:
                stops_count = len(sub_path['stop_list'])
                total_stops += stops_count
                current_fare_stage = sub_path['stop_list'][0]["Fare_stage"]
                # Initial fare stages for each sub-path
                total_ac_fare += 10  # Base fare for AC
                total_non_ac_fare += 5  # Base fare for non-AC

                for stop in sub_path['stop_list']:
                    fare_stage = stop["Fare_stage"]
                    

                    # Accumulate fares for the path
                    total_ac_fare += abs(fare_stage - current_fare_stage) * 5
                    total_non_ac_fare += abs(fare_stage - current_fare_stage) * 5
                    current_fare_stage = fare_stage
            # Append summary data to the path
            path.append({
                "changes": changes,
                "total_stops": total_stops,
                "total_ac_fare": total_ac_fare,
                "total_non_ac_fare": total_non_ac_fare
            })
        
        return paths
