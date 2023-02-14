ERROR_MSG = {
	403 : "권한이 없습니다.",
	404 : "데어터가 없습니다.",
	4041 : "같은 이름의 음식이 있습니다.",
	4042 : "카테고리의 이름을 다시 확인해 주세요"
}

SUCCESS_MSG = {
	200 : "성공",
	204 : "데이터가 없습니다",
}

def error_msg(error_code : int = 0, serializer = None,):
	if serializer:
		return {'error_msg' : serializer.errors}
	else :
		msg = ERROR_MSG[error_code]
		return {"error_msg" : msg}


def success_msg(success_code: int = 0):
	msg = SUCCESS_MSG[success_code]
	return {'success_msg' : msg} 