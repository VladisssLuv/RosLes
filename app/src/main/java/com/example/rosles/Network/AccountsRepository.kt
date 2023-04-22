package com.example.rosles.Network

import com.example.rosles.RequestClass.AuthRequest
import com.example.rosles.RequestClass.PerechetRequest
import com.example.rosles.RequestClass.RegistrationReqest
import com.example.rosles.RequestClass.UpdateRequest
import com.example.rosles.ResponceClass.*
import com.squareup.moshi.Moshi
import okhttp3.ResponseBody
import retrofit2.Call
import retrofit2.Retrofit
import retrofit2.http.GET


interface AccountsSource {


    suspend fun getUNDER():UNDER_RESP
    suspend fun getBREED():BREED_RESP
    suspend fun getQUATER():QUATER_RESP
    suspend fun getDISTRICTFORESTLY():DISTRICTFORESTLY_RESP
    suspend fun getFORESTLY():FORESTLY_RESP
    suspend fun getSUBJECTRF():SUBJECTRF_RESP
    suspend fun getLISTREGION():LISTREGION_RESP
    suspend fun getSAMPLE():SAMPLE_RESP
    suspend fun getLIST():LIST_RESP


    suspend fun reproduction(): ReproductionResp
    suspend fun perechet(perechetRequest: PerechetRequest): BaseResp
    suspend fun registration(registrationReqest: RegistrationReqest): BaseResp
    suspend fun getrequestsubjectRF(): SubjectResp
    suspend fun forestlubyid(id:Int): ForestlyResp
    suspend fun districtbyID(id:Int): DistrictResp
    suspend fun quaterdistrictbyID(id:Int): CvartalResp
    suspend fun getprofile():getUserResp
    suspend fun getbreed():BreedResp
    suspend fun getbd():BaseResp
    suspend fun get_user(body:AuthRequest):AuthReSponce
    suspend fun upload(body: UpdateRequest): BaseResp


    //suspend fun roleRequst(): responceRole

    fun getCurrentToken(): String?
    fun setCurrentToken(token: String?)
}


class AccountsRepository( private val accountsSource: AccountsSource) {


    suspend fun getUNDER():UNDER_RESP=accountsSource.getUNDER()
    suspend fun getBREED():BREED_RESP=accountsSource.getBREED()
    suspend fun getQUATER():QUATER_RESP=accountsSource.getQUATER()
    suspend fun getDISTRICTFORESTLY():DISTRICTFORESTLY_RESP=accountsSource.getDISTRICTFORESTLY()
    suspend fun getFORESTLY():FORESTLY_RESP=accountsSource.getFORESTLY()
    suspend fun getSUBJECTRF():SUBJECTRF_RESP=accountsSource.getSUBJECTRF()
    suspend fun getLISTREGION():LISTREGION_RESP=accountsSource.getLISTREGION()
    suspend fun getSAMPLE():SAMPLE_RESP=accountsSource.getSAMPLE()
    suspend fun getLIST():LIST_RESP=accountsSource.getLIST()


    suspend fun reproduction(): List<GETReproductionResp> = accountsSource.reproduction().get

    suspend fun perechet(perechetRequest: PerechetRequest): BaseResp =  accountsSource.perechet(perechetRequest)

    suspend fun registration (registrationReqest: RegistrationReqest):BaseResp = accountsSource.registration(registrationReqest)

    suspend fun getprofile(): getUserResp =  accountsSource.getprofile()

    suspend fun getrequestsubjectRF():SubjectResp=accountsSource.getrequestsubjectRF()

    suspend fun forestlubyid(id:Int):ForestlyResp=accountsSource.forestlubyid(id)

    suspend fun districtbyID(id:Int):DistrictResp=accountsSource.districtbyID(id)

    suspend fun quaterdistrictbyID(id:Int):CvartalResp=accountsSource.quaterdistrictbyID(id)

    suspend fun getbreed():BreedResp=accountsSource.getbreed()

    suspend fun get_user(body: AuthRequest):AuthReSponce=accountsSource.get_user(body)

    suspend fun upload(body: UpdateRequest):BaseResp=accountsSource.upload(body)

    suspend fun getbd():BaseResp=accountsSource.getbd()




//    suspend fun roleRequest():List<GetResp> {
//        var resp=try {
//            accountsSource.roleRequst().get
//        } catch (e: BackendException) {
//            // user with such email already exists
//            if (e.code == 409) throw AccountAlreadyExistsException(e)
//            else throw e
//        }
//        return resp
//    }
}
