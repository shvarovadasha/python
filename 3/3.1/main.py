with open("ospf.txt") as file:
    for line in file:
        fields = line.strip().split()
        protocol = "OSPF"
        prefix = fields[1]
        ad_metric = fields[2].strip("[]")
        next_hop = fields[4].strip(",")
        last_update = fields[5].strip(",")
        outbound_interface = fields[6]

        output = f"""
        Protocol:           {protocol}
        Prefix:             {prefix}
        AD/Metric:          {ad_metric}
        Next-Hop:           {next_hop}
        Last update:        {last_update}
        Outbound Interface: {outbound_interface}
        """
        print(output)
