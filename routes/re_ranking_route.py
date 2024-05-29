from fastapi import APIRouter, Depends, status
from configs.security import UnauthorizedMessage, get_token
from configs.logger import logger
from controllers.cross_encoder import CrossEncoderModel
from models.re_ranking_model import ReRankingModel
from utils.exception_handling import handle_exceptions
import numpy as np

re_ranking_route = APIRouter(tags=['Re_Ranking'])

cross_encoder = CrossEncoderModel()

@re_ranking_route.post(
    "/re-ranking", 
    responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)},
    status_code=status.HTTP_200_OK
    )
@handle_exceptions
async def re_rank(
    body:ReRankingModel,
    token_auth: str = Depends(get_token)
    ):
    body = body.model_dump()
    pairs_qa = [[body['question'], content] for content in body['content']]
    rerank = cross_encoder.predict(pairs_qa)
    rerank_index = np.argpartition(rerank, -body['top_k'])[-body['top_k']:]
    logger.info('Re ranking successfully')
    return {
        "message": "success",
        "rerank_index": rerank_index.tolist(),
    }
    
@re_ranking_route.get(
    "/re-ranking/warmup", 
    responses={status.HTTP_401_UNAUTHORIZED: dict(model=UnauthorizedMessage)},
    status_code=status.HTTP_200_OK
    )
@handle_exceptions
async def re_rank_warmup(
    token_auth: str = Depends(get_token)
    ):
    logger.info('Warming up the model')
    cross_encoder.predict([["warm", "up"]])
    logger.info('Warmup success')
    return {
        "message": "warmup success"
    }
