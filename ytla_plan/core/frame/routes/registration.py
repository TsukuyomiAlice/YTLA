def register_all_blueprints(app):
    from core.frame.routes.routeUpload import upload_bp
    from core.frame.routes.routeGlobalPersistence import globalPersistence_bp
    from core.cards.routes.routeCards import cards_bp
    from core.plans.routes.routePlans import plans_bp
    from core.modules.routes.routeModules import modules_bp

    app.register_blueprint(upload_bp)
    app.register_blueprint(globalPersistence_bp)
    app.register_blueprint(cards_bp)
    app.register_blueprint(plans_bp)
    app.register_blueprint(modules_bp)

    from features.languageEnglish.routes.routeModuleAssessment import language_assessment_bp
    from features.languageEnglish.routes.routeModuleDictionary import language_dictionary_bp
    from features.languageEnglish.routes.routeModuleVocabulary import language_vocabulary_bp

    app.register_blueprint(language_assessment_bp)
    app.register_blueprint(language_dictionary_bp)
    app.register_blueprint(language_vocabulary_bp)