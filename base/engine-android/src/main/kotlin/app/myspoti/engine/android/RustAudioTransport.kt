package app.myspoti.engine.android

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.json.JSONObject

internal object RustAudioTransport {
    init { System.loadLibrary("orpheon_audio") }

    private external fun fetchNative(url: String, headers: String, start: Long, end: Long): ByteArray

    suspend fun fetch(url: String, headers: Map<String, String>, range: LongRange): ByteArray =
        withContext(Dispatchers.IO) {
            fetchNative(url, JSONObject(headers).toString(), range.first, range.last)
        }
}
