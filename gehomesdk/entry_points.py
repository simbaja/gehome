import argparse
from asyncio import gather

from .gather_data import gather_appliance_data

def appliance_data():
    parser = argparse.ArgumentParser()

    parser.add_argument('-u', '--username', type=str, required=True, 
                        help="Your SmartHQ Username") 
    parser.add_argument('-p', '--password', type=str, required=True,
                        help="Your SmartHQ Password")
    parser.add_argument('-r', '--region', type=str, choices=["US","EU"], default="US",
                        help="Your SmartHQ Region")

    args = parser.parse_args()

    gather_appliance_data(args.username, args.password, args.region)
