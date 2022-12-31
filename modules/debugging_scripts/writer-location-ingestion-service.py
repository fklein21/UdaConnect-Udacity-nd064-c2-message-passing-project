
import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
Used for debugging the gRPC location ingestion endpoint.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:30020")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
location = location_pb2.LocationMessage(
    person_id=1,
    latitude="11.45",
    longitude="49.7",
)


response = stub.Create(location)
