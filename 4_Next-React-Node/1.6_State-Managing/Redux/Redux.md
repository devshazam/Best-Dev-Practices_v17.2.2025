
https://www.youtube.com/watch?v=ETWABFYv0GM&list=PL6DxKON1uLOHsBCJ_vVuvRsW84VnqmPp6&index=9
    https://github.dev/utimur/react-redux-typescript-course

import {useDispatch, useSelector} from "react-redux";


// получить
    const state = useSelector((state:any) => state.cash.cash);


// задать
    const dispatch = useDispatch();
    const callD = () => {
        dispatch({type: "ADD_CASH", payload: 3})
    }