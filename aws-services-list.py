# 1) The list should be empty to start
aws_services = []

# 2) Populate list with append
aws_services.append('EC2')
aws_services.append('RDS')
aws_services.append('S3')

# 2.1) Populate list with insert
aws_services.insert(3, 'CloudFront')

# 2.2 Extend the list
aws_services.extend(['VPC', 'SNS', 'Beanstalk', 'Lambda', 'Autoscaling', 'IAM'])

# 3) Print the list and the length
print("Top 10 used AWS Services: ")
print(aws_services)
print("Total of most used services: ", len(aws_services))

# 4) Remove 5 services from the list by name or by list
aws_services[9:] = []
del aws_services[1]

# 5) Print new list and the new length
print("Top 8 used AWS Services: ")
print(aws_services)
print("Total of most used AWS Services: ", len(aws_services))
