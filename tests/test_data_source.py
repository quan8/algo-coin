
class TestDataSource:
    def setup(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_StreamingDataSource(self):
        from data_source import StreamingDataSource
        from callback import Callback

        try:
            x = StreamingDataSource()
            assert False
        except:
            pass

        class Test(StreamingDataSource):
            def run(self, engine):
                pass

        class TestCB(Callback):
            def onMatch(self):
                pass

            def onReceived(self):
                pass

            def onOpen(self):
                pass

            def onDone(self):
                pass

            def onChange(self):
                pass

            def onError(self):
                pass

            def onAnalyze(self):
                pass

        try:
            t = Test()

            t.registerCallback(TestCB())
            assert t._callbacks
            assert len(t._callbacks) == 7
            assert len(t._callbacks['ERROR']) == 1

        except:
            assert False