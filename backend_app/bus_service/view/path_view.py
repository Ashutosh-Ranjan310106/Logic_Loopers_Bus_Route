
from flask import render_template
from bus_service.service.service import BusService
class path_view:
    def render_path(paths):
        for path in paths:
            total_stops = 0
            changes = len(path)
            total_ac_fare = 0
            total_non_ac_fare = 0
            starting_stops_list = []
            for sub_path in path:
                stops_count = len(sub_path['stop_list'])
                total_stops += stops_count
                current_fare_stage = sub_path['stop_list'][0]["Fare_stage"]
                sub_path['bus_no'] = sub_path['stop_list'][0]["bus_no"]
                starting_stops_list.append(sub_path['stop_list'][0]["stop_id"])
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
            

            bus_timings = BusService.get_recent_buses(stop_ids=starting_stops_list)
            for index, sub_path in enumerate(path):
                sub_path['bus_timings']=[]
                print(sub_path.keys())
                for timing in bus_timings[sub_path['stop_list'][0]['stop_name']]:
                    if timing[2] == sub_path['direction'][0]:
                        sub_path['bus_timings'].append(str(timing[0]))
                if not sub_path['bus_timings']:
                    sub_path['bus_timings'].append('no buses are avlable now ')
            path.append({
                "changes": changes-1,
                "total_stops": total_stops,
                "total_ac_fare": total_ac_fare,
                "total_non_ac_fare": total_non_ac_fare
            })

        return render_template('bus_paths.html', paths=paths)
