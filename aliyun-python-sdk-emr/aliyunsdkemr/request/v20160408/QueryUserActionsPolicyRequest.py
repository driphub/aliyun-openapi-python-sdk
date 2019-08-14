# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkemr.endpoint import endpoint_data

class QueryUserActionsPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'QueryUserActionsPolicy','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceId(self):
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self,ResourceId):
		self.add_query_param('ResourceId',ResourceId)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)

	def get_ActionNameLists(self):
		return self.get_query_params().get('ActionNameLists')

	def set_ActionNameLists(self,ActionNameLists):
		for i in range(len(ActionNameLists)):	
			if ActionNameLists[i] is not None:
				self.add_query_param('ActionNameList.' + str(i + 1) , ActionNameLists[i]);

	def get_AliyunUserId(self):
		return self.get_query_params().get('AliyunUserId')

	def set_AliyunUserId(self,AliyunUserId):
		self.add_query_param('AliyunUserId',AliyunUserId)