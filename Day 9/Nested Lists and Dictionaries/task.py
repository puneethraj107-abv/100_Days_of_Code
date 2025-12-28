capitals = {"france":"paris",
            "germany":"berlin"
}
print(capitals["germany"])

#nested List in dictionary
travel_log={
    "france":["paris","lile","dijon"],
    "germany":["stuttgart", "berlin"]
}
print(travel_log["france"][1])

#nesting list inside list
nested_list=["a", "b",["c","d"]]
print(nested_list[2][0])

#nested dictionary in a dictionary
travellog={
    "france":{
        "cities_visited":["paris","lille","dijon"],
        "total_visits":12

    },
    "germany":{
        "cities_visited":["berlin","stuttgart","hamburg"],
        "total_visits":5
    }
}
print(travellog["germany"]["cities_visited"][1])
print(travellog["france"]["total_visits"])